type MouseRand struct {
        n   int
        buf [64]byte
        tmp [24]byte
        f   *os.File
        h   hash.Hash
}

func New(n int) (*MouseRand, error) {
        f, err := os.Open(fmt.Sprintf("/dev/input/event%d", n))
        if err != nil {
                return nil, err
        }

        h := sha512.New()
        r := &MouseRand{f: f, h: h}
        return r, nil
}

func (r *MouseRand) Close() {
        r.f.Close()
}

func (r *MouseRand) Seed(seed int64) {
        binary.LittleEndian.PutUint64(r.tmp[:0], uint64(seed))
        r.h.Reset()
        r.h.Write(r.buf[:])
        r.h.Write(r.tmp[:8])
        r.h.Sum(r.buf[:0])
        r.n = 64
}

func (r *MouseRand) Int63() int64 {
        return int64(r.Uint64() >> 1)
}

func (r *MouseRand) Uint64() uint64 {
        if r.n == 0 {
                _, err := r.f.Read(r.tmp[:])
                if err != nil {
                        panic(err) // FIXME
                }

                r.h.Reset()
                r.h.Write(r.buf[:])
                r.h.Write(r.tmp[:])
                r.h.Sum(r.buf[:0])
                r.n = 64
        }

        r.n -= 8
        return binary.LittleEndian.Uint64(r.buf[r.n:])
}
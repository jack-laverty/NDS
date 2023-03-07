
import redis
import arinc424.record as a424

if __name__ == '__main__':
    db = redis.Redis(host='localhost', port=6379, db=0)

    file = './input/airport'
    with open(file) as f:
        for line in f.readlines():
            q = 0
            r = a424.Record()
            if r.validate(line):
                if r.read(line):
                    q += 1
                    db.set(q, r.json(False))

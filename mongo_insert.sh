mongo --eval 'use my_database; db.counters.insert({"id": "user_id", seq: 0});'
mongo --eval 'use my_database; db.counters.find();'
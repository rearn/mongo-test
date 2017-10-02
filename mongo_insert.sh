mongo my_database --eval 'db.counters.insert({"id": "user_id", seq: 0});'
mongo my_database --eval 'db.counters.find();'
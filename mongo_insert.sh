mongo my_database --eval 'db.createUser({user:"test", pwd:"passwd", rolse: [{role:"readWrite", db:"counters"}]});'
mongo my_database --eval 'db.my_database.counters.insert({"id": "user_id", seq: 0});'
mongo my_database --eval 'db.my_database.counters.find();'

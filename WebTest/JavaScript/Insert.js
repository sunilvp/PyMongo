
use secondChapter
db.secondChapterCollection.drop()

var insertDoc = {"name": "jsInsert", "insert" :"Random insert from js"};
db.secondChapterCollection.insert(insertDoc);


var inserted = db.secondChapterCollection.findOne();
db.secondChapterCollection.insert(inserted);


for (i =1;i<=10;i++){
	var forInsertDoc = {"name": "jsInsert:"+i, "insert" :"Random insert from js :"+i, "value" : i};
	db.secondChapterCollection.insert(forInsertDoc);
}

print( db.secondChapterCollection.find({'value' : {$gt :5}}))
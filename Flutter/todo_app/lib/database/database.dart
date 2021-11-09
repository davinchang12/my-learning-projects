import 'dart:io';

import 'package:path_provider/path_provider.dart';
import 'package:sqflite/sqflite.dart';
import 'package:todo_app/models/todo.dart';

class DBProvider {
  DBProvider._();
  static DBProvider db = DBProvider._();

  static Database? _database;
  
  Future<Database> get database async =>
    _database ??= await initDB();

  Future<Database> initDB() async {
    Directory documentsDirectory = await getApplicationDocumentsDirectory();
    String path = documentsDirectory.path + "ToDo.db";
    return await openDatabase(path, version: 1, onOpen: (db) {
    }, onCreate: (Database db, int version) async {
      await db.execute("CREATE TABLE ToDo ("
          "id INTEGER PRIMARY KEY,"
          "todo_list TEXT"
          ")");
    });
  }

  newToDo(ToDo newToDo) async {
    final db = await database;
    var res = await db.insert("ToDo", newToDo.toMap());
    return res;
  }

  getAllToDo() async {
    final db = await database;
    var res = await db.query("ToDo");
    List<ToDo> list = res.isNotEmpty ? res.map((e) => ToDo.fromMap(e)).toList() : [];
    return list;
  }

  getToDo(int id) async {
    final db = await database;
    var res = await db.query("ToDo", where: "id = ?", whereArgs: [id]);
    return res.isNotEmpty ? ToDo.fromMap(res.first) : Null;
  }

  deleteToDo(int id) async {
    final db = await database;
    db.delete("ToDo", where: "id = ?", whereArgs: [id]);
  }

}
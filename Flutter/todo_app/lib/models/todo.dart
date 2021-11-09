import 'dart:convert';

ToDo todoFromJson(String str) {
  final jsonData = json.decode(str);
  return ToDo.fromMap(jsonData);
}

String todoToJson(ToDo data) {
  final dyn = data.toMap();
  return json.encode(dyn);
}

class ToDo {
  int id;
  String todoList;

  ToDo({required this.id, required this.todoList});

  factory ToDo.fromMap(Map<String, dynamic> json) => ToDo(
    id: json["id"],
    todoList: json["todo_list"]
  );

  Map<String, dynamic> toMap() => {
    "id": id,
    "todoList": todoList
  };
}

List<ToDo> testToDos = [
    ToDo(id: 1, todoList: "eat"),
    ToDo(id: 2, todoList: "drink"),
  ];

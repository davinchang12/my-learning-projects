final String tableTodo = 'todo';
final String columnId = '_id';
final String columnTitle = 'title';
final String columnDescription = 'description';

class Todo {
  late int id;
  late String title;
  late String description;

  Map<String, Object?> toMap() {
    var map = <String, Object?>{
      columnTitle: title,
      columnDescription: description
    };
    if (id != null) {
      map[columnId] = id;
    }
    return map;
  }

  Todo({
    required this.id,
    required this.title,
    required this.description,
  });

  Todo.fromMap(Map<String, dynamic> map) {
    id = map[columnId];
    title = map[columnTitle];
    description = map[columnDescription];
  }
}
import 'package:flutter/material.dart';
import 'package:todo_app/database/database.dart';
import 'package:todo_app/models/todo.dart';
import 'package:todo_app/widgets/card.dart';
import 'package:todo_app/widgets/content_view.dart';

class HomePage extends StatelessWidget {
  const HomePage({ Key? key }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("ToDo"),),
      body: ContentView(
        color: Colors.green,
        child: FutureBuilder<dynamic>(
          future: DBProvider.db.getAllToDo(),
          builder: (context, snapshot) {
            if(snapshot.hasData) {
              return ListView.builder(
                itemCount: snapshot.data!.length,
                itemBuilder: (BuildContext context, int index) {
                  ToDo todo = snapshot.data![index];
                  return CustomCard(todoContent: todo.todoList);
                }
              );
            } else {
              return Center(child: CircularProgressIndicator());
            }
          }
        ),
      ),
      floatingActionButton: FloatingActionButton(
        child: Icon(Icons.add),
        onPressed: () async {
          ToDo rnd = testToDos[0];
          await DBProvider.db.newToDo(rnd);
        },
      ),
    );
  }
}
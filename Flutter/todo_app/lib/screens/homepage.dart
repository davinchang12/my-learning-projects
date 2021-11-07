import 'package:flutter/material.dart';
import 'package:todo_app/widgets/card.dart';

class HomePage extends StatelessWidget {
  const HomePage({ Key? key }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Column(
      children: const [
        Text("ToDo App"),
        CustomCard(todoContent: "Drink"),
      ],
    );
  }
}
import 'package:flutter/material.dart';

class CustomCard extends StatelessWidget {
  final String todoContent;

  const CustomCard({required this.todoContent, Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 5,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(10),
      ),
      color: Colors.black,
      child: Container(
        margin: const EdgeInsets.all(10),
        child: Row(
          children: [
            Text(
              todoContent,
              style: const TextStyle(
                color: Colors.white
              ),
            ),
          ],
        ),
      ),
    );
  }
}

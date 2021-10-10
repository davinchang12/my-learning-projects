import 'package:flutter/material.dart';
import 'package:submission_dicoding/main_screen/main_screen.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        canvasColor: Color(0xff171717),
      ),
      home: MainScreen(),
    );
  }
}
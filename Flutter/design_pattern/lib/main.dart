import 'package:design_pattern/theme.dart';
import 'package:flutter/material.dart';

import 'package:design_pattern/constant.dart';
import 'package:design_pattern/router.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Design Pattern App',
      theme: lightTheme,
      onGenerateRoute: RouterCustom.generateRoute,
      initialRoute: initialRoute,
      debugShowCheckedModeBanner: false,
    );
  }
}
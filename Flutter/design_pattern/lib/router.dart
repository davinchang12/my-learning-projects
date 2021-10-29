import 'package:design_pattern/constant.dart';
import 'package:design_pattern/screens/category/category.dart';
import 'package:design_pattern/screens/main_menu/main_menu.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class RouterCustom {
  static Route<dynamic> generateRoute(RouteSettings settings) {
    switch (settings.name) {
      case initialRoute:
        return MaterialPageRoute(
          builder: (_) => MainMenu(),
        );
      
      case categoryRoute:
        return MaterialPageRoute(
          builder: (_) => Category(),
        );

      default:
        return MaterialPageRoute(
          builder: (_) => MainMenu(),
        );
    }
  }
}
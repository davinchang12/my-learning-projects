import 'package:design_pattern/constant.dart';
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
      default:
        return MaterialPageRoute(
          builder: (_) => MainMenu(),
        );
    }
  }
}
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import 'package:design_pattern/constant.dart';
import 'package:design_pattern/data/models/design_pattern.dart';
import 'package:design_pattern/data/models/design_pattern_category.dart';
import 'package:design_pattern/screens/category/category.dart';
import 'package:design_pattern/screens/design_pattern_details/design_pattern_details.dart';
import 'package:design_pattern/screens/main_menu/main_menu.dart';
import 'package:design_pattern/widgets/introduction/introduction.dart';
import 'package:design_pattern/widgets/chapter_1/chapter_1.dart';

class RouterCustom {
  static Route<dynamic> generateRoute(RouteSettings settings) {
    switch (settings.name) {
      case initialRoute:
        return MaterialPageRoute(
          builder: (_) => MainMenu(),
        );
      
      case categoryRoute:
        var category = settings.arguments as DesignPatternCategory;
        return MaterialPageRoute(
          builder: (_) => Category(
            category: category,
          ),
        );

      case _DesignPatternRoutes.introductionRoute:
        var designPattern = settings.arguments as DesignPattern;
        return MaterialPageRoute(
          builder: (_) => DesignPatternDetails(
            designPattern: designPattern,
            example: const Introduction(),
          ),
        );
      
      case _DesignPatternRoutes.chapter1Route:
        var designPattern = settings.arguments as DesignPattern;
        return MaterialPageRoute(
          builder: (_) => DesignPatternDetails(
            designPattern: designPattern,
            example: const Chapter1(),
          ),
        );

      default:
        return MaterialPageRoute(
          builder: (_) => MainMenu(),
        );
    }
  }
}

class _DesignPatternRoutes {
  static const String introductionRoute = '/introduction';
  static const String chapter1Route = '/chapter_1';
}
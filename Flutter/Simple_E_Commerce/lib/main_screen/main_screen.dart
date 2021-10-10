import 'package:flutter/material.dart';

import 'package:submission_dicoding/main_screen/main_screen_header.dart';
import 'package:submission_dicoding/main_screen/main_screen_items.dart';

class MainScreen extends StatelessWidget{

  @override
  Widget build(BuildContext context){
    return Scaffold(
      body: Column(
        children: [
          MainScreenHeader(),
          MainScreenItems(),
        ]
      )
    );
  }
}
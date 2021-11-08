import 'package:flutter/material.dart';

class ContentView extends StatelessWidget {
  Color color;
  Widget child;

  ContentView({
    required this.color, 
    required this.child,
    Key? key }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(10),
      margin: const EdgeInsets.all(10),
      decoration: BoxDecoration(
        color: color,
        border: Border.all(
          color: color,
        ),
        borderRadius: const BorderRadius.all(Radius.circular(20))
      ),
      child: child,
    );
  }
}
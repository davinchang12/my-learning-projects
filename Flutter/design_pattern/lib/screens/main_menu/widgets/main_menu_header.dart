import 'package:flutter/material.dart';

class MainMenuHeader extends StatelessWidget {
  const MainMenuHeader({ Key? key }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            'Design Pattern',
            style: TextStyle(
              fontSize:36,
              fontWeight: FontWeight.bold
            ),
          ),
          const SizedBox(height:12),
          Text(
            'with Flutter',
            style: TextStyle(
              fontSize:24,
            ),
          )
        ],
      ),
    );
  }
}
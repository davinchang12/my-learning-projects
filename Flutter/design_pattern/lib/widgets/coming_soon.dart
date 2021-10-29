import 'package:flutter/material.dart';

import 'package:design_pattern/constant.dart';

class ComingSoon extends StatelessWidget {
  const ComingSoon({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.only(top: paddingXL),
      child: Center(
        child: Text(
          'Coming Soon!',
          style: Theme.of(context).textTheme.headline3!.copyWith(
                color: Colors.white70,
              ),
        ),
      ),
    );
  }
}

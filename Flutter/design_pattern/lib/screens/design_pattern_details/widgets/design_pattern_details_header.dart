import 'package:flutter/material.dart';
import 'package:flutter/foundation.dart';

import 'package:design_pattern/constant.dart';
import 'package:design_pattern/data/models/design_pattern.dart';

class DesignPatternDetailsHeader extends StatelessWidget {
  final DesignPattern designPattern;

  const DesignPatternDetailsHeader({
    required this.designPattern,
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Column(
      children: <Widget>[
        Row(
          children: <Widget>[
            Text(
              designPattern.title,
              style: Theme.of(context).textTheme.headline3!.copyWith(
                    fontSize: 32.0,
                  ),
            ),
          ],
        ),
        const SizedBox(height: spaceL),
        Row(
          children: <Widget>[
            Expanded(
              child: Text(
                designPattern.description,
                style: Theme.of(context).textTheme.subtitle1,
                textAlign: TextAlign.justify,
                overflow: TextOverflow.ellipsis,
                maxLines: 99,
              ),
            ),
          ],
        ),
      ],
    );
  }
}
import 'package:flutter/material.dart';

import 'package:design_pattern/constant.dart';
import 'package:design_pattern/data/models/design_pattern.dart';
import 'package:design_pattern/widgets/selection_card.dart';

class DesignPatternCard extends StatelessWidget {
  final DesignPattern designPattern;

  const DesignPatternCard({required this.designPattern, Key? key})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    var contentHeader = Text(
      designPattern.title,
      style: Theme.of(context).textTheme.headline3!.copyWith(
            fontSize: 26.0,
          ),
      overflow: TextOverflow.ellipsis,
    );
    var contentText = Text(
      designPattern.description,
      style: Theme.of(context).textTheme.bodyText1,
      textAlign: TextAlign.justify,
      overflow: TextOverflow.ellipsis,
      maxLines: 2,
    );
    onSelectionCardTap() => Navigator.pushNamed(
          context,
          designPattern.route,
          arguments: designPattern,
        );

    return SelectionCard(
      backgroundColor: lightBackgroundColor,
      backgroundHeroTag: "${designPattern.id}_background",
      contentHeader: contentHeader,
      contentText: contentText,
      onTap: onSelectionCardTap,
    );
  }
}

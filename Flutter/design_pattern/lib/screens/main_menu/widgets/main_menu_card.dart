import 'package:design_pattern/constant.dart';
import 'package:design_pattern/data/models/design_pattern_category.dart';
import 'package:design_pattern/widgets/selection_card.dart';
import 'package:flutter/material.dart';

class MainMenuCard extends StatelessWidget {
  final DesignPatternCategory category;

  const MainMenuCard({required this.category, Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    var contentHeader = Text(
      category.title,
      style: Theme.of(context)
          .textTheme
          .headline3!
          .copyWith(fontSize: 26, color: Colors.white),
      overflow: TextOverflow.ellipsis,
    );

    var contentText = Text(
      category.patterns.length == 1
          ? '${category.patterns.length} pattern'
          : '${category.patterns.length} patterns',
      style: Theme.of(context).textTheme.subtitle1!.copyWith(
            color: Colors.white,
          ),
    );

    onSelectionCardTap() => Navigator.pushNamed(
          context,
          categoryRoute,
          arguments: category,
        );

    return SelectionCard(
        backgroundColor: Color(category.color),
        backgroundHeroTag: "${category.id}_background",
        contentHeader: contentHeader,
        contentText: contentText,
        onTap: onSelectionCardTap);
  }
}

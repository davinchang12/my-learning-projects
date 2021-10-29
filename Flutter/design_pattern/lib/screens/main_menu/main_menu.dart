import 'package:flutter/material.dart';

import 'package:design_pattern/constant.dart';

import 'package:design_pattern/data/models/design_pattern_category.dart';
import 'package:design_pattern/data/repositories/design_pattern_categories_repository.dart';

import 'package:design_pattern/screens/main_menu/widgets/main_menu_card.dart';
import 'package:design_pattern/screens/main_menu/widgets/main_menu_header.dart';

class MainMenu extends StatelessWidget {
  final DesignPatternCategoriesRepository repository = DesignPatternCategoriesRepository();

  MainMenu({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(paddingL),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const MainMenuHeader(), 
              FutureBuilder<List<DesignPatternCategory>>(
                future: repository.get(),
                initialData: const [],
                builder: (
                  _, 
                  snapshot,
                ) {
                  if (snapshot.hasData) {
                    return Column(
                      children: [
                        for (var category in snapshot.data!) 
                          Container(
                            margin: const EdgeInsets.only(top: marginL),
                            child: MainMenuCard(
                              category: category,
                            ),
                          )
                      ],
                    );
                  }

                  return CircularProgressIndicator(
                    backgroundColor: lightBackgroundColor,
                    valueColor: AlwaysStoppedAnimation<Color>(
                      Colors.black.withOpacity(0.65)
                    ),
                  );
                }
              ),
            ],
          ),
        ),
      ),
    );
  }
}

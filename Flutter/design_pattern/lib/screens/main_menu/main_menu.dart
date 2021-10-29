import 'package:flutter/material.dart';

import 'package:design_pattern/constant.dart';

import 'package:design_pattern/data/models/design_pattern_category.dart';
import 'package:design_pattern/data/repositories/design_pattern_categories_repository.dart';

import 'package:design_pattern/screens/main_menu/widgets/main_menu_card.dart';
import 'package:design_pattern/screens/main_menu/widgets/main_menu_header.dart';

class MainMenu extends StatelessWidget {
  final DesignPatternCategoriesRepository repository = DesignPatternCategoriesRepository();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: SingleChildScrollView(
          padding: EdgeInsets.all(10),
          child: Column(
            children: [
              MainMenuHeader(), 
              FutureBuilder<List<DesignPatternCategory>>(
                future: repository.get(),
                initialData: [],
                builder: (
                  _, 
                  snapshot,
                ) {
                  if (snapshot.hasData) {
                    return Column(
                      children: [
                        for (var category in snapshot.data!) 
                          Container(
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

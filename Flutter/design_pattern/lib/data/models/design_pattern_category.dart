import 'package:design_pattern/data/models/design_pattern.dart';

class DesignPatternCategory {
  final String id;
  final String title;
  final int color;
  final List<DesignPattern> patterns;

  DesignPatternCategory({
    required this.id,
    required this.title,
    required this.color,
    required this.patterns,
  });

  factory DesignPatternCategory.fromJson(Map<String, dynamic> json) {
    var designPatternJsonList = json['patterns'] as List;
    var designPatternList = designPatternJsonList
        .map((designPatternJson) => DesignPattern.fromJson(designPatternJson))
        .toList();

    return DesignPatternCategory(
      id: json['id'],
      title: json['title'],
      color: int.parse(json['color']),
      patterns: designPatternList,
    );
  }
}

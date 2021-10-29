import 'package:design_pattern/constant.dart';

import 'package:flutter/services.dart' show rootBundle;

class MarkdownRepository {
  Future<String> get(String designPatternId) async {
    var path = '$markdownPath$designPatternId.md';
    var markdownString = await rootBundle.loadString(path);

    return markdownString;
  }
}
import 'package:flutter/material.dart';
import 'package:flutter_colorpicker/flutter_colorpicker.dart';
import 'package:provider/provider.dart';
import 'package:theme_color_provider/theme_provider.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (context) => ThemeProvider(),
      child: Consumer<ThemeProvider>(
        builder: (context, themeProvider, child) => MaterialApp(
          title: 'Flutter Demo',
          theme: ThemeData(
            primarySwatch: Colors.blue,
          ),
          home: const MainScaffold(),
        ),
      ),
    );
  }
}

class MainScaffold extends StatelessWidget {
  const MainScaffold({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: _ThemedAppBar(
        title: const Text('Theme provider example'),
        actions: [
          IconButton(
            icon: const Icon(Icons.colorize),
            onPressed: () => _showColorPicker(context),
          ),
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceAround,
          children: [
            Consumer<ThemeProvider>(
              builder: (context, themeProvider, child) => Text(
                'Text',
                style: Theme.of(context).textTheme.headline2?.copyWith(
                      color: themeProvider.mainColor,
                    ),
              ),
            ),
            Consumer<ThemeProvider>(
              builder: (context, themeProvider, child) => Text(
                'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                style: Theme.of(context).textTheme.bodyText2?.copyWith(
                      color: themeProvider.mainColor,
                    ),
              ),
            ),
            Consumer<ThemeProvider>(
              builder: (context, themeProvider, child) => Container(
                height: 100,
                width: 100,
                decoration: BoxDecoration(
                  color: themeProvider.mainColor,
                  borderRadius: const BorderRadius.all(
                    Radius.circular(50),
                  ),
                ),
              ),
            ),
            Consumer<ThemeProvider>(
              builder: (context, themeProvider, child) => Slider(
                activeColor: themeProvider.mainColor,
                inactiveColor: themeProvider.mainColor.withOpacity(0.5),
                value: 0,
                onChanged: (newValue) {},
              ),
            ),
            Consumer<ThemeProvider>(
              builder: (context, themeProvider, child) => Switch(
                activeColor: themeProvider.mainColor,
                value: true,
                onChanged: (newValue) {},
              ),
            ),
          ],
        ),
      ),
    );
  }

  void _showColorPicker(BuildContext context) {
    ThemeProvider themeProvider =
        Provider.of<ThemeProvider>(context, listen: false);
    showDialog(
        context: context,
        builder: (context) => AlertDialog(
              titlePadding: const EdgeInsets.all(0.0),
              contentPadding: const EdgeInsets.all(0.0),
              content: Wrap(
                children: [
                  ColorPicker(
                    pickerColor: themeProvider.mainColor,
                    onColorChanged: (color) =>
                        themeProvider.changeThemeColor(color),
                  ),
                ],
              ),
              actions: [
                TextButton(
                  onPressed: () {
                    Navigator.of(context).pop();
                  },
                  child: const Text('Close'),
                )
              ],
            ));
  }
}

class _ThemedAppBar extends StatelessWidget with PreferredSizeWidget {
  final Widget? title;
  final List<Widget>? actions;
  @override
  final Size preferredSize;

  _ThemedAppBar({
    Key? key,
    this.title,
    this.actions,
  })  : preferredSize = const Size.fromHeight(kToolbarHeight),
        super(key: key);

  @override
  Widget build(BuildContext context) {
    return Consumer<ThemeProvider>(
      builder: (context, themeProvider, child) => AppBar(
        title: title,
        actions: actions,
        backgroundColor: themeProvider.mainColor,
      ),
    );
  }
}

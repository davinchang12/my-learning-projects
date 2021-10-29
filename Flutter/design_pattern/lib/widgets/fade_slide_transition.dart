import 'package:flutter/material.dart';

class FadeSlideTransition extends StatelessWidget {
  final AnimationController controller;
  final Tween<Offset> slideAnimationTween;
  final Widget child;
  final double begin;
  final double end;
  final int index;
  final double singleItemDurationInterval;

  const FadeSlideTransition(
      {required this.controller,
      required this.slideAnimationTween,
      required this.child,
      this.begin = 0.0,
      this.end = 1.0,
      this.index = -1,
      this.singleItemDurationInterval = -1,
      Key? key})
      : super(key: key);

  double get _begin => index != -1 && singleItemDurationInterval != -1
      ? _calculateBegin()
      : begin;

  double get _end =>
      index != -1 && singleItemDurationInterval != -1 ? _calculateEnd() : end;

  double _calculateBegin() {
    var delay = (singleItemDurationInterval * index).toDouble();

    return begin + delay < 1.0
        ? begin + delay
        : 1.0 - singleItemDurationInterval;
  }

  double _calculateEnd() {
    var delay = (singleItemDurationInterval * index).toDouble();

    return begin + delay < 1.0
        ? begin + delay
        : 1.0 - singleItemDurationInterval;
  }

  Animation<double> get _fadeAnimation => Tween<double>(
        begin: 0.0,
        end: 1.0,
      ).animate(
        CurvedAnimation(
          parent: controller,
          curve: Interval(_begin, _end, curve: Curves.ease),
        ),
      );

  Animation<Offset> get _slideAnimation => slideAnimationTween.animate(
        CurvedAnimation(
            parent: controller,
            curve: Interval(
              _begin,
              _end,
              curve: Curves.ease,
            )),
      );

  @override
  Widget build(BuildContext context) {
    return FadeTransition(
      opacity: _fadeAnimation,
      child: SlideTransition(
        position: _slideAnimation,
        child: child,
      ),
    );
  }
}

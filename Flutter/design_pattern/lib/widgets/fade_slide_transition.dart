import 'package:flutter/material.dart';

class FadeSlideTransition extends StatelessWidget {
  final AnimationController controller;
  final Tween<Offset> slideAnimationTween;
  final Widget child;
  final double begin;
  final double end;
  final int index;
  final double singleItemDurationInterval;

  FadeSlideTransition(
      {required this.controller,
      required this.slideAnimationTween,
      required this.child,
      this.begin = 0.0,
      this.end = 1.0,
      required this.index,
      required this.singleItemDurationInterval,
      Key? key})
      : super(key: key);

  Animation<double> get _fadeAnimation => Tween<double>(
        begin: 0.0,
        end: 1.0,
      ).animate(
        CurvedAnimation(
          parent: controller,
          curve: Interval(begin, end, curve: Curves.ease),
        ),
      );

  Animation<Offset> get _slideAnimation => slideAnimationTween.animate(
        CurvedAnimation(
            parent: controller,
            curve: Interval(
              begin,
              end,
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

import 'dart:math';
import 'package:flame/components.dart';
import 'package:flame/events.dart';
import 'package:flame/game.dart';
import 'package:flame/extensions.dart';
import 'package:flutter/material.dart';

class ConveyorBelt extends PositionComponent {
  ConveyorBelt(Vector2 gameSize)
      : super(
            size: Vector2(gameSize.x, 20),
            position: Vector2(0, gameSize.y / 2 - 10),
            anchor: Anchor.topLeft);

  @override
  void render(Canvas canvas) {
    final paint = Paint()..color = Colors.grey.shade800;
    canvas.drawRect(size.toRect(), paint);
  }
}

class RecyclingBin extends PositionComponent {
  final Color color;

  RecyclingBin({
    required this.color,
    required Vector2 position,
    required Vector2 size,
  }) : super(
          position: position,
          size: size,
          anchor: Anchor.center,
        );

  @override
  void render(Canvas canvas) {
    final paint = Paint()..color = color;
    canvas.drawRect(size.toRect(), paint);
  }

  bool checkIfItemDroppedInside(RecyclableItem item) {
    return item.color == color && toRect().contains(item.position.toOffset());
  }
}

class RecyclableItem extends PositionComponent
    with DragCallbacks, HasGameRef<RecyclingGame> {
  final Color color;
  final Vector2 gameSize;
  final double speed; // Units per second
  bool isDragged = false;

  RecyclableItem({
    required this.color,
    required this.gameSize,
    required Vector2 position,
    required Vector2 size,
    this.speed = 100.0, // Default speed
  }) : super(
          position: position,
          size: size,
          anchor: Anchor.center,
        );

  @override
  void render(Canvas canvas) {
    final paint = Paint()..color = color;
    canvas.drawCircle(Offset.zero, size.x / 2, paint);
  }

  @override
  void update(double dt) {
    super.update(dt);
    if (!isDragged) {
      position.add(Vector2(speed * dt, 0));
      if (position.x > gameSize.x) {
        removeFromParent();
      }
    }
  }

  @override
  void onDragStart(DragStartEvent event) {
    super.onDragStart(event);
    isDragged = true;
  }

  @override
  void onDragUpdate(DragUpdateEvent event) {
    position.setFrom(event.canvasEndPosition - size);
  }

  @override
  void onDragEnd(DragEndEvent event) {
    super.onDragEnd(event);
    isDragged = false;
    (gameRef).checkForItemDropInBin(this);
  }
}

class RecyclingGame extends FlameGame {
  final Random rng = Random();
  final double itemSpawnRate = 1.0;
  double timeUntilNextSpawn = 0.0;
  final List<RecyclingBin> bins = [];

  @override
  Future<void> onLoad() async {
    final conveyorBelt = ConveyorBelt(size);
    add(conveyorBelt);

    bins.addAll([
      RecyclingBin(
          color: Colors.red,
          position: Vector2(100, size.y / 1.4),
          size: Vector2(100, 100)),
      RecyclingBin(
          color: Colors.green,
          position: Vector2(size.x - 50, size.y / 2.4),
          size: Vector2(100, 100)),
    ]);

    bins.forEach(add);
  }

  @override
  void update(double dt) {
    super.update(dt);

    timeUntilNextSpawn -= dt;
    if (timeUntilNextSpawn <= 0) {
      spawnRecyclableItem();
      timeUntilNextSpawn = itemSpawnRate;
    }
  }

  void spawnRecyclableItem() {
    final Vector2 startPosition = Vector2(0, size.y / 2);
    final Vector2 itemSize = Vector2(50, 50);
    final List<Color> colors = [Colors.red, Colors.green, Colors.blue];
    final Color color = colors[rng.nextInt(colors.length)];

    final RecyclableItem item = RecyclableItem(
      gameSize: size,
      color: color,
      position: startPosition,
      size: itemSize,
    );
    add(item);
  }

  void checkForItemDropInBin(RecyclableItem item) {
    for (final bin in bins) {
      if (bin.checkIfItemDroppedInside(item)) {
        item.removeFromParent();
        break;
      }
    }
  }
}

void main() {
  runApp(GameWidget(game: RecyclingGame()));
}

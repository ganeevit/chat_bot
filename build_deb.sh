#!/bin/bash
set -e
PACKAGE=telegram-weather-bot
VERSION=1.0
BUILD_DIR=build/$PACKAGE

rm -rf "$BUILD_DIR"
mkdir -p "$BUILD_DIR/DEBIAN"
mkdir -p "$BUILD_DIR/usr/share/$PACKAGE"
mkdir -p "$BUILD_DIR/usr/bin"

cat > "$BUILD_DIR/DEBIAN/control" <<CONTROL
Package: $PACKAGE
Version: $VERSION
Section: misc
Priority: optional
Architecture: all
Depends: python3, python3-requests, python3-telegram
Maintainer: Example <example@example.com>
Description: Simple Telegram bot that shows weather forecast using Yandex Weather
CONTROL

install -m 644 bot.py "$BUILD_DIR/usr/share/$PACKAGE/bot.py"
cat > "$BUILD_DIR/usr/bin/$PACKAGE" <<'WRAPPER'
#!/bin/sh
exec python3 /usr/share/telegram-weather-bot/bot.py "$@"
WRAPPER
chmod 755 "$BUILD_DIR/usr/bin/$PACKAGE"

dpkg-deb --build "$BUILD_DIR" > /dev/null

echo "Package created: $BUILD_DIR.deb"


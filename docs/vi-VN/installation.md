---
title: Cài đặt
description: Cài đặt argvus-ai và tìm hiểu cách mỗi tác nhân được cung cấp.
---

## Cài đặt gói

Trên Arch Linux với các kho ARGVUS được cấu hình, một khi `argvus-ai` được xuất bản ở đó:

```sh
sudo pacman -S argvus-ai
```

Đối với bản dựng cục bộ chưa được xuất bản, hãy chạy `make validate` và `make build` trong kho lưu trữ nguồn `argvus-ai`, sau đó cài đặt `.pkg.tar.zst` thu được từ `build/dist/` với `sudo pacman -U /path/to/package.pkg.tar.zst`. Pacman phải có khả năng giải quyết các phần phụ thuộc của nó, bao gồm cả gói `argvus` chính.Gói phần mềm yêu cầu `argvus`, `rofi`, `jq`, `mise`, `opencode` và `openai-codex`; Arch cung cấp `/bin/sh` thông qua `bash`. OpenCode chạy dưới dạng `opencode`, và gói `openai-codex` cung cấp `codex`.

## Tích hợp máy tính để bàn

Sử dụng các gói `argvus-hyprland` và `argvus-taskbar` đã được cập nhật. Hyprland tải mô-đun Lua tùy chọn được cung cấp bởi `argvus-ai`. Hook Pacman của tích hợp này làm mới cấu hình hệ thống tiêu chuẩn sau khi cài đặt hoặc gỡ bỏ. Một cấu hình root tùy chỉnh hoặc việc tự động tải lại bị vô hiệu hóa có thể yêu cầu việc tải lại rõ ràng. Các ghi đè phím tắt cá nhân hiện có vẫn giữ quyền ưu tiên.

Máy chiếu `argvus-appearance` được cập nhật giữ lại mô-đun thanh tác vụ và tuân thủ **Trung tâm điều khiển > Giao diện > Thanh tác vụ > Biểu tượng > Mô-đun tùy chọn > Tác nhân AI**. Tùy chọn này được bật theo mặc định; nhấp **Áp dụng** sau khi thay đổi. Bật nó không cài đặt các tác nhân.

## Claude Code khi sử dụng lần đầu

Chọn Claude Code từ bộ chọn Rofi hoặc trình khởi chạy ứng dụng. Terminal ARGVUS sẽ mở và chạy `mise install claude` với tư cách người dùng thường của bạn nếu không tìm thấy phiên bản đã cài đặt. Cần có truy cập mạng cho lần cài đặt đầu tiên này. Bộ bao (wrapper) sẽ xác định tệp thực thi đã cài đặt và thêm thư mục của nó vào PATH của tiến trình được khởi chạy; nó không chỉnh sửa tệp khởi động shell hay cài đặt với quyền root. Các lần khởi động sau sẽ tái sử dụng cài đặt này.

## Xóa

```sh
sudo pacman -R argvus-ai
```

Module Lua thuộc sở hữu gói và các mục nhập trên máy tính để bàn đã bị xóa, và module thanh tác vụ sẽ ẩn khi trợ lý của nó vắng mặt. Cấu hình Hyprland tiêu chuẩn tự động tải lại để xóa liên kết. Các công cụ mise, cài đặt đại lý và chứng thực do người dùng sở hữu được giữ lại. Pacman không tự động xóa các phụ thuộc của đại lý với lệnh này.

Gói AI ARGVUS không cài đặt các tác nhân bên ngoài tại thời điểm cài đặt gói. Hermes, Cursor CLI và Kimi cài đặt trong lần khởi chạy đầu tiên; dữ liệu người dùng của họ vẫn nằm ngoài gói. Xem hướng dẫn sử dụng để biết hướng dẫn gỡ bỏ.

---
title: Usage and troubleshooting
description: Chọn tác nhân, điều khiển biểu tượng thanh tác vụ và chẩn đoán các tích hợp bị thiếu.
---

## Mở một tác nhân

Nhấn **SUPER + A**, nhấp vào rô-bốt trên thanh tác vụ hoặc chọn mục ứng dụng của một tác nhân. Bộ chọn cung cấp các cài đặt OpenCode/Codex có thể thực thi và cung cấp Claude Code cho cài đặt lần đầu khi mise tồn tại. **Esc** hủy mà không khởi chạy hoặc tải xuống bất cứ thứ gì.

Thiết bị đầu cuối kế thừa thư mục làm việc của người gọi; khởi chạy đồ họa thường bắt đầu từ thư mục chính của phiên. Bắt đầu một tác nhân từ thiết bị đầu cuối của dự án khi bạn cần một thư mục làm việc cụ thể.

## Khả năng hiển thị của thanh tác vụMở **Trung tâm điều khiển > Giao diện > Thanh tác vụ > Biểu tượng > Mô-đun tùy chọn**, bật **Tác nhân AI**, sau đó **Áp dụng**. Robot thuộc về `group/right-2`; nếu ngăn của nó bị thu gọn, hãy mở rộng nhóm tiện ích. Tùy chọn là `/taskbar/icons/ai_agents_enabled`, mặc định là true, và vẫn giữ sau khi tái tạo. Nó chỉ kiểm soát biểu tượng: các lối tắt và mục trên màn hình vẫn khả dụng. Khả năng sẵn sàng khi chạy vẫn có thể ẩn một biểu tượng đã bật.

## Các lệnh chẩn đoán

```sh
argvus-ai list
argvus-ai status
argvus-ai status --check
argvus-ai menu
argvus-ai launch opencode
argvus-ai launch codex
argvus-ai launch claude
```

`list` chỉ báo cáo các tác nhân đã cài đặt. `status` xuất JSON của Waybar, trong khi `status --check` báo cáo liệu có tùy chọn menu đã cài đặt hoặc có thể cài đặt thông qua trạng thái thoát của nó. Chỉ việc chọn/khởi chạy Claude mới có thể bắt đầu cài đặt; `run-claude` là điểm vào terminal nội bộ.

If the shortcut still uses the old combination, inspect its personal override in Control Center's keyboard shortcuts page; packaged defaults do not overwrite it. If the robot disappears after applying appearance settings, update `argvus-appearance` and regenerate/apply the taskbar settings. Avoid editing generated Waybar/Luatập tin trực tiếp.Nếu cài đặt Claude thất bại, kiểm tra lỗi trên terminal, truy cập mạng và phiên bản mise đã cài, sau đó chọn lại Claude. Các truy vấn mise chạy từ home nên cấu hình theo dự án sẽ không chọn công cụ khác. Wrapper không yêu cầu các shim mise trong PATH đồ họa. Phát hiện OpenCode/Codex sử dụng PATH đồ họa, không dùng alias shell hoặc script khởi động tương tác.

Quay lại [AI Agents](/docs/argvus-ai/). Các tác nhân

mở trong một cửa sổ Kitty nổi được căn giữa có tiêu đề `ARGVUS AI Agent`, với đầu và chân trang ARGVUS. Nhấn **Ctrl + E** để đóng cửa sổ tác nhân. Phím tắt này được khung giữ; Esc và Ctrl+C vẫn có sẵn cho tác nhân.

Hồ sơ Kitty chuyên dụng `ai-agents` ẩn các tab và xóa các phím tắt thừa kế cho tab, chia cửa sổ và toàn màn hình. Các phím tắt Clipboard Ctrl+Shift+C và Ctrl+Shift+V vẫn có sẵn. Cấu hình được tạo ra của nó là `kitty-tui/kitty-ai-agents.conf` dưới thư mục cache ARGVUS. Gói module Hyprland nổi và căn giữa cửa sổ với lớp `argvus-ai` ở 1399 × 920.

## Uninstalling agents

`argvus-ai list` shows installed agents. Run `argvus-ai uninstall` to select an ARGVUS-managed Hermes, Cursor CLI, or Kimi installation, then confirm removal. You can also run `argvus-ai uninstall hermes`, `argvus-ai uninstall cursor`, or `argvus-ai uninstall kimi`. Installations made outside ARGVUS are left untouched, except a legacy Cursor CLI install is recognized by the explicit Cursor command when `~/.local/bin/agent` resolves inside `~/.local/share/cursor-agent/versions/`. Hermes uses its official uninstaller. Cursor and Kimi binaries are removed while user settings, sessions, and credentials are preserved.

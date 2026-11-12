---
title: Cách sử dụng và khắc phục sự cố
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

Nếu phím tắt vẫn sử dụng tổ hợp cũ, hãy kiểm tra ghi đè cá nhân của phím tắt đó trong trang phím tắt của Trung tâm Kiểm soát; mặc định được đóng gói không ghi đè lên nó. Nếu rô-bốt biến mất sau khi áp dụng cài đặt giao diện, hãy cập nhật `argvus-appearance` và tạo lại/áp dụng cài đặt trên thanh tác vụ. Tránh chỉnh sửa được tạo Waybar/Luatập tin trực tiếp. Nếu cài đặt Claude thất bại, hãy kiểm tra lỗi trên thiết bị đầu cuối, truy cập mạng và phiên bản mise đã cài đặt, sau đó chọn lại Claude. Truy vấn mise chạy từ nhà nên cấu hình dự án sẽ không chọn công cụ khác. Trình bao bọc không yêu cầu miếng chêm mise trong đồ họa PATH. Phát hiện OpenCode/Codex sử dụng đồ họa PATH, không sử dụng bí danh shell hoặc script khởi động tương tác.

Quay lại [AI Agents](/docs/argvus-ai/). Các tác nhân

mở trong một cửa sổ Kitty nổi được căn giữa có tiêu đề `ARGVUS AI Agent`, với đầu và chân trang ARGVUS. Nhấn **Ctrl + E** để đóng cửa sổ tác nhân. Phím tắt này được khung giữ; Esc và Ctrl+C vẫn có sẵn cho tác nhân.

Hồ sơ Kitty chuyên dụng `ai-agents` ẩn các tab và xóa các phím tắt thừa kế cho tab, chia cửa sổ và toàn màn hình. Các phím tắt Clipboard Ctrl+Shift+C và Ctrl+Shift+V vẫn có sẵn. Cấu hình được tạo ra của nó là `kitty-tui/kitty-ai-agents.conf` dưới thư mục cache ARGVUS. Gói module Hyprland nổi và căn giữa cửa sổ với lớp `argvus-ai` ở 1399 × 920.

## Gỡ cài đặt tác nhân

`argvus-ai list` hiển thị các tác nhân đã cài đặt. Chạy `argvus-ai uninstall`, chọn bản cài Hermes, Cursor CLI hoặc Kimi do ARGVUS quản lý rồi xác nhận gỡ bỏ. Bạn cũng có thể chạy trực tiếp `argvus-ai uninstall hermes`, `argvus-ai uninstall cursor` hoặc `argvus-ai uninstall kimi`. Các bản cài bên ngoài ARGVUS không bị thay đổi, ngoại trừ Cursor CLI cũ được lệnh Cursor chỉ định nhận diện nếu `~/.local/bin/agent` trỏ đến bên trong `~/.local/share/cursor-agent/versions/`. Hermes dùng trình gỡ chính thức. Tệp thực thi Cursor và Kimi được xóa, còn thiết lập, phiên và thông tin xác thực của người dùng được giữ lại.

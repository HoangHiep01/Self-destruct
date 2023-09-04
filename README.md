# Tự hủy

## Lời nói đầu

 Vào một ngày, tôi chợt nghĩ tới sự vô thường ở đời và cũng lại nghĩ tới những con quỷ theo sau. Yeah!
 Máy tính có những thứ cần phải xóa.

## Ý tưởng

 Xóa files, folders tại lần mở máy cách lần gần nhất trước đó x ngày. Tôi lựa chọn x = 14 do ý tưởng cũng một phần xuất phát từ [Fake My History](idea).

 Cứ mỗi khi mở máy, kiểm tra xem lần khởi động này cách lần gần nhất đã quá x ngày chưa.
 - Nếu quá: xóa các files, folders trong danh sách phần setting. Có nên để đoạn mã tự xóa nó là một nhiệm vụ cuối không nhờ?
 - Ngược lại: Cập nhật thời gian khởi động mới.


## Tip, Exp

 Chuyển script tới thư mục Startup để script tự động chạy khi mở máy:
 - Nhấn tổ hợp `Win + R`
 - Gõ `shell:startup`
 - Click `OK`

 Đổi phần mở rộng từ .py sang .pyw sẽ giúp script chạy ở nền (không hiển thị console).

 Không nên để `setting` vào thư mục Startup vì thư mục này sẽ mở khi script chạy (thử nghiệm trên máy của tôi).

 Do dấu `\` là ký tự đặc biệt nên khi viết đường dẫn trong file code thì hay viết thành `\\`.

## Sử dụng

 Ở dòng 6 trong file main.py, hãy điền đường dẫn đây đủ tới thư mục setting. Ví dụ: SETTING_PATH = "C:\\folder1\\folder2\\folder3\\setting".

 Tương tự với dòng 7 trong file main.py, hãy điền đường dẫn đây đủ tới thư mục Startup. 
 Ví dụ trên win11: SCRIPT_PATH = "C:\\Users\\`%usename%`\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\main.py". `%usename%` là tên người dùng trên máy của bạn.

 Cuối cùng là chuyển thư mục setting và file main.py tới đúng vị trí đường dẫn đã điền.

 Ngoài ra, ở dòng 112 file main:
 - self_destruct=False có nghĩa là không xóa thư mục setting và file main nếu sự kiện xóa các thư mục, file xảy ra (thử nghiệm nên để self_destruct=False).

 - self_destruct=True thì ngược lại và đây là giá trị mặc định (nếu xóa self_destruct=False ở dòng 112 đi thì script tự hiểu là self_destruct=True).

## Chú ý

 Tương đối hoàn thiện.

 Vẫn đang thử nghiệm.





[idea]: https://press.opera.com/2023/07/27/opera-gx-unveils-fake-my-history/

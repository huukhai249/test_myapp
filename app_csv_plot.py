
import csv
import matplotlib.pyplot as plt



FILE_CSV = "du_lieu_ban_hang.csv"
FILE_ANH = "bieu_do_ban_hang_heheh.png"


def doc_du_lieu_csv():
    days = []
    sales = []
    #haifapof

    #afhaihf

    with open(FILE_CSV, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        # Bỏ qua hàng tiêu đề
        
        next(reader)
        for row in reader:
            day = row[0].strip()
            quantity = int(row[1])

            days.append(day)
            sales.append(quantity)

    return days, sales


def ve_bieu_do(days, sales):
    """Vẽ biểu đồ cột và lưu thành ảnh PNG."""
    plt.figure(figsize=(10, 6))
    plt.bar(days, sales)

    plt.title("BIỂU ĐỒ SỐ LƯỢNG SẢN PHẨM BÁN TRONG TUẦN")
    plt.xlabel("Ngày")
    plt.ylabel("Số lượng sản phẩm")
    plt.grid(axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout()
    plt.savefig(FILE_ANH, dpi=300)
    plt.show()


def main():
    try:
        # 1. Đọc dữ liệu từ file CSV.
        days, sales = doc_du_lieu_csv()

        # 2. Tính toán kết quả.
        total_sales = sum(sales)
        max_sales = max(sales)
        best_day = days[sales.index(max_sales)]

        # 3. In kết quả ra màn hình.
        print("----- BÁO CÁO BÁN HÀNG -----")
        print(f"Tổng số sản phẩm bán trong tuần: {total_sales}")
        print(f"Ngày bán nhiều nhất: {best_day}")
        print(f"Số lượng bán cao nhất: {max_sales}")
        print(f"Đã lưu biểu đồ tại: {FILE_ANH}")

        # 4. Vẽ và lưu biểu đồ.
        ve_bieu_do(days, sales)

    except FileNotFoundError:
        print("Không tìm thấy file du_lieu_ban_hang.csv.")
        print("Hãy đặt file CSV cùng thư mục với chương trình.")

    except ValueError as error:
        print(f"Dữ liệu không hợp lệ: {error}")


if __name__ == "__main__":
    main()

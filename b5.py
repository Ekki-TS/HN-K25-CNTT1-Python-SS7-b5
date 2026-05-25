# INPUT: Dữ liệu lô hàng được lưu dưới dạng chuỗi
raw_batch = " LAP-VN-23-001 ; mou-us-24-012 ; KEY-vn-23-abc ; lap-JP-22-045 ; MOn-vn-24-099 "

while True:

    # OUTPUT: Hiển thị menu chức năng
    print("\n===== HỆ THỐNG GIẢI MÃ DỮ LIỆU KHO HÀNG =====")
    print("1. Hiển thị chuỗi mã vạch gốc")
    print("2. Giải mã, làm sạch và in báo cáo kiểm kê")
    print("3. Tra cứu nhanh theo đuôi Serial")
    print("4. Thoát chương trình")

    # INPUT: Người dùng nhập lựa chọn menu
    choice = input("Nhập lựa chọn của bạn: ").strip()
    if not choice.isdigit():
        # OUTPUT: Thông báo lỗi nếu nhập chữ hoặc ký tự đặc biệt
        print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-4!")
        continue
    choice = int(choice)
    if choice == 1:
        # OUTPUT: In chuỗi mã vạch gốc
        print("\nChuỗi mã vạch gốc:")
        print(raw_batch)
    elif choice == 2:
        products = raw_batch.split(";")
        success_count = 0
        total_count = 0
        # OUTPUT: In báo cáo
        print(f"{'MÃ SP':<10} {'XUẤT XỨ':<10} {'NĂM SX':<10} {'SERIAL':<10} {'TRẠNG THÁI'}")
        for product in products:
            clean_product = product.strip().upper()
            parts = clean_product.split("-")
            product_code = parts[0]
            country = parts[1]
            year = "20" + parts[2]
            serial = parts[3]
            total_count += 1
            if serial.isdigit():
                status = "Pass"
                success_count += 1
            else:
                status = "Lỗi Serial - Reject"
            # OUTPUT: In thông tin sản phẩm
            print(f"{product_code:<10} {country:<10} {year:<10} {serial:<10} {status}")

        # OUTPUT: In tổng kết kiểm kê
        print(f"\nĐã giải mã thành công {success_count} sản phẩm hợp lệ / Tổng số {total_count} sản phẩm.")
    elif choice == 3:

        # INPUT: Người dùng nhập 2 số cuối serial
        search_serial = input("Nhập 2 số cuối của Serial cần tìm: ").strip()
        products = raw_batch.split(";")
        found = False
        for product in products:
            clean_product = product.strip().upper()
            parts = clean_product.split("-")
            product_code = parts[0]
            country = parts[1]
            year = "20" + parts[2]
            serial = parts[3]
            if serial[-2:] == search_serial:

                # OUTPUT: In thông tin sản phẩm tìm thấy
                print("\nTìm thấy sản phẩm:")
                print(f"MÃ SP: {product_code}")
                print(f"XUẤT XỨ: {country}")
                print(f"NĂM SX: {year}")
                print(f"SERIAL: {serial}")
                found = True
        if found == False:
            # OUTPUT: Thông báo không tìm thấy
            print("Không tìm thấy sản phẩm phù hợp")
    elif choice == 4:
        # OUTPUT: Thông báo kết thúc
        print("Đóng ca kiểm kho. Chào tạm biệt!")
        break
    else:
        # OUTPUT: Thông báo nếu nhập ngoài phạm vi 1-4
        print("Chức năng không tồn tại, vui lòng nhập số từ 1-4!")

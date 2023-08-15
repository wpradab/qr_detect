import cv2


def extract_qr_codes(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    detector = cv2.QRCodeDetector()
    retval, decoded_info, points, _ = detector.detectAndDecodeMulti(blurred_image)

    qr_codes = []
    if retval:
        for qr_code_data in decoded_info:
            qr_code_data = qr_code_data.strip()
            qr_codes.append(qr_code_data)

    return qr_codes

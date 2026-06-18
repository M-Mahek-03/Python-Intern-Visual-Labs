import cv2
import face_recognition
import numpy as np
import csv
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class FaceRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition Attendance System")

        self.video_capture = cv2.VideoCapture(0)
        self.known_faces = self.load_known_faces()
        self.students = self.known_faces.copy()
        self.recognition_started = False

        self.create_widgets()

    def create_widgets(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10)

        self.video_label = tk.Label(self.main_frame)
        self.video_label.pack()

        self.start_button = tk.Button(self.main_frame, text="Start Attendance", command=self.start_attendance)
        self.start_button.pack(pady=5)

        self.quit_button = tk.Button(self.main_frame, text="Quit", command=self.root.quit)
        self.quit_button.pack(pady=5)

    def load_known_faces(self):
        danish_image = face_recognition.load_image_file("photos/danish.jpeg")
        danish_encodings = face_recognition.face_encodings(danish_image)[0]

        nadeem_image = face_recognition.load_image_file("photos/nadeem.jpeg")
        nadeem_encodings = face_recognition.face_encodings(nadeem_image)[0]

        unais_image = face_recognition.load_image_file("photos/unais.jpeg")
        unais_encodings = face_recognition.face_encodings(unais_image)[0]

        known_face_encodings = [
            tuple(danish_encodings),
            tuple(nadeem_encodings),
            tuple(unais_encodings)
        ]

        known_face_names = [
            "Danish",
            "Nadeem",
            "Unais"
        ]

        return dict(zip(known_face_encodings, known_face_names))

    def start_attendance(self):
        if not self.recognition_started:
            self.recognition_started = True
            self.capture_frames()

    def capture_frames(self):
        _, frame = self.video_capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(list(self.known_faces.keys()), face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(list(self.known_faces.keys()), face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_faces[list(self.known_faces.keys())[best_match_index]]

            cv2.rectangle(frame, (left * 4, top * 4), (right * 4, bottom * 4), (0, 255, 0), 2)
            cv2.putText(frame, name, (left * 4, top * 4 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

            if name in self.students:
                self.students.remove(name)
                self.mark_attendance(name)

        photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
        self.video_label.configure(image=photo)
        self.video_label.image = photo

        if self.recognition_started:
            self.root.after(10, self.capture_frames)

    def mark_attendance(self, student_name):
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H-%M-%S")
        with open(current_date + '.csv', 'a', newline='') as f:
            lnwriter = csv.writer(f)
            lnwriter.writerow([student_name, current_time])


def main():
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()


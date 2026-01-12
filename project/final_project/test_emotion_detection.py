from EmotionDetection import emotion_detector

def test_emotion_detection():
    statements = [
        ("I am glad this happened", "joy"),
        ("I am really mad about this", "anger"),
        ("I feel disgusted just hearing about this", "disgust"),
        ("I am so sad about this", "sadness"),
        ("I am really afraid that this will happen", "fear")
    ]
    
    for statement, expected_emotion in statements:
        result = emotion_detector(statement)
        dominant_emotion = result["dominant_emotion"]
        print(f"Statement: {statement}")
        print(f"Expected: {expected_emotion}, Detected: {dominant_emotion}")
        assert dominant_emotion == expected_emotion, "Test failed!"
    
    print("All tests passed successfully!")

if __name__ == "__main__":
    test_emotion_detection()

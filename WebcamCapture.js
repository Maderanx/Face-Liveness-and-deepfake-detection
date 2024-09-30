// src/WebcamCapture.js
import React, { useRef, useEffect, useState } from 'react';
import axios from 'axios';

function WebcamCapture() {
    const videoRef = useRef(null);
    const [livenessResult, setLivenessResult] = useState('');

    useEffect(() => {
        startWebcam();
    }, []);

    const startWebcam = () => {
        navigator.mediaDevices.getUserMedia({ video: true })
            .then((stream) => {
                videoRef.current.srcObject = stream;
            })
            .catch((err) => {
                console.error("Error accessing webcam: ", err);
            });
    };

    const captureFrame = async () => {
        const canvas = document.createElement('canvas');
        canvas.width = videoRef.current.videoWidth;
        canvas.height = videoRef.current.videoHeight;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(videoRef.current, 0, 0, canvas.width, canvas.height);
        
        const imageData = canvas.toDataURL('image/jpeg');
        
        // Send the frame to the Streamlit backend
        try {
            const response = await axios.post('http://localhost:8501/process-frame', { image: imageData });
            setLivenessResult(response.data.result);
        } catch (error) {
            console.error("Error sending frame: ", error);
        }
    };

    return (
        <div>
            <h1>Face Liveness Detection</h1>
            <video ref={videoRef} autoPlay playsInline width="640" height="480"></video>
            <br />
            <button onClick={captureFrame}>Check Liveness</button>
            {livenessResult && <h2>{livenessResult}</h2>}
        </div>
    );
}

export default WebcamCapture;

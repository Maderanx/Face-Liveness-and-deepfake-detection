# Saycool-Sight-Face-Liveness
DL based Face Liveness detector

# Proposed Solution​

Saycool integrates both passive and active face liveness detection models to ensure robust and secure authentication.​

# Working​

# Passive Model:​

Initially, the system evaluates facial features such as texture, skin reflection, micro-expressions, etc. to detect liveness without user interaction.​
3D CNN Model  - Used to create the passive detection model, since a 3D CNN can capture temporal and spatial features from clips and also help in deepfake detection compared to 2D CNN models.

# Active Model:​

If the passive model does not achieve the required confidence level, the system prompts the user to perform random facial expressions (e.g., Tilting head, blinking at different speeds) to verify liveness and help eliminate deepfakes.​

LSTM Model – Used to create the active detection model, since LSTM can remember previous frames to check if someone is performing an action in real-time.​

The system provides instructions for the required actions in multiple languages to ensure accessibility and ease of use for users from different linguistic backgrounds.​

from skimage import io, filters
import matplotlib.pyplot as plt
from pathlib import Path

# --------------------------------------------------
# paths
# --------------------------------------------------

filename = "drain_imbib-Stitched_final.tif"
# filename = "drain_imbib-Stitched_t0.tif"

currentDir = Path.cwd()
input_path = currentDir / filename
output_dir = currentDir / "threshold_results"
output_dir.mkdir(exist_ok=True)

# --------------------------------------------------
# image
# --------------------------------------------------

# Load grayscale image
image = io.imread(input_path, as_gray=True)

# Apply local threshold
block_size = 35   # size of the neighborhood around each pixel
local_thresh = filters.threshold_local(image, block_size, offset=10)

# Binarize the image
binary_local = image > local_thresh

# --------------------------------------------------
# paths
# --------------------------------------------------


# Show results
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(image, cmap='gray')
ax[0].set_title("Original")
ax[1].imshow(binary_local, cmap='gray')
ax[1].set_title("Local Thresholding")
plt.show()


# io.imsave(str(output_dir/filename)+"/local_thresholding.png" ,binary_local.astype('uint8') * 255)
io.imsave(output_dir / f"{filename}_local_thresholding.png",
          (binary_local.astype('uint8') * 255))
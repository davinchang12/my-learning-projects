# Library importing
import os
import shutil

class FileOrganization():
	def organize(self, current_dir, destination_dir, ext):
		# Search for all file in the current directory
		for file in os.listdir(current_dir):
			# Get file name and file extension from each file in the current directory
			filename, file_ext = os.path.splitext(file)

			# Check if destination directory is exists
			if not os.path.exists(destination_dir):
				os.makedirs(destination_dir)

			# Move the file using shutil from current directory to destination directory
			if not file_ext:
				pass

			elif file_ext in (ext):
				shutil.move(
					os.path.join(current_dir, (filename + file_ext)),
					os.path.join(destination_dir,  (filename + file_ext))
				)					

	def getExtension(self, current_dir):
		# Return all available extensions in the folder
		return list(set([os.path.splitext(file)[1] for file in os.listdir(current_dir) if os.path.splitext(file)[1] != '']))
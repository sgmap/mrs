/* global fetch, FormData */

class FileSelect {
  constructor (putUrl, csrftoken) {
    this.errorMsg = {
      mimeType: 'Mime type not valid',
      fileSize: 'File too large'
    }
    this.validMimeTypes = [
      'image/jpeg'
    ]
    this.maxFileSize = Math.pow(10, 7) // 10 MB
    this.putUrl = putUrl
    this.csrfToken = csrftoken
  }

  // file mime type (string)
  // private, tested through this.validateFile
  mimeTypeValidate (mimeType) {
    return this.validMimeTypes.indexOf(mimeType) >= 0
  }

  // file size (bytes)
  // private, tested through this.validateFile
  fileSizeValidate (size) {
    return size <= this.maxFileSize
  }

  // file object
  isFileValid (file) {
    if (!this.mimeTypeValidate(file.type)) {
      this.error(this.errorMsg.mimeType)
      return false
    }

    if (!this.fileSizeValidate(file.size)) {
      this.error(this.errorMsg.fileSize)
      return false
    }

    return true
  }

  // file = file object
  async putRequest (file) {
    const data = new FormData()
    data.append('file', file)

    const headers = {
      'X-CSRFToken': this.csrfToken,
      'content-type': ''
    }

    const putOptions = {
      method: 'POST',
      headers,
      body: data
    }

    return await fetch(this.putUrl, putOptions)
  }

  // delete url for file (string)
  async deleteRequest (deleteUrl) {
    const deleteOptions = {
      method: 'DELETE'
    }

    return await fetch(deleteUrl, deleteOptions)
  }

  // file = file object
  async upload (file) {
    // request
    if (this.isFileValid(file)) {
      try {
        const resp = await this.putRequest()

        this.success(file, resp)
      } catch (e) {
        // request error (only take httpError)
        this.error(e)
      }
    }
  }

  // file = file object
  // response = ajax response
  success (file, response) {
    // Add file <li>
    console.log('success')
  }

  // error => error exception
  error (error) {
    // Add error <li>
    console.log('error')
  }
}

module.exports = FileSelect

import React, { useState } from 'react';
import { useDropzone } from 'react-dropzone';
import { fileService } from '../services/fileService';
import { CircularProgress, Button } from '@material-ui/core';

const FileUpload = () => {
    const [files, setFiles] = useState([]);
    const [uploading, setUploading] = useState(false);

    const { getRootProps, getInputProps } = useDropzone({
        accept: 'application/pdf',
        onDrop: acceptedFiles => {
            setFiles(acceptedFiles.map(file => Object.assign(file, {
                preview: URL.createObjectURL(file)
            })));
        }
    });

    const uploadFiles = async () => {
        setUploading(true);
        try {
            await Promise.all(files.map(file => fileService.uploadFile(file)));
            setFiles([]);
        } catch (error) {
            console.error('Error uploading files:', error);
        } finally {
            setUploading(false);
        }
    };

    return (
        <div {...getRootProps({ className: 'dropzone' })}>
            <input {...getInputProps()} />
            <p>Drag 'n' drop PDF files here, or click to select files</p>
            <Button variant="contained" color="primary" onClick={uploadFiles} disabled={uploading}>
                {uploading ? <CircularProgress size={24} /> : 'Upload'}
            </Button>
            <aside>
                <h4>Files</h4>
                <ul>
                    {files.map(file => (
                        <li key={file.path}>
                            {file.path} - {file.size} bytes
                        </li>
                    ))}
                </ul>
            </aside>
        </div>
    );
};

export default FileUpload;
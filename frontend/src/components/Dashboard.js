import React, { useEffect, useState } from 'react';
import { Card, Col, Row, Statistic } from 'antd';
import { fileService } from '../services/fileService';

const Dashboard = () => {
  const [fileStats, setFileStats] = useState({
    totalFiles: 0,
    processedFiles: 0,
    pendingFiles: 0,
  });

  useEffect(() => {
    fetchFileStats();
  }, []);

  const fetchFileStats = async () => {
    try {
      const stats = await fileService.getFileStats();
      setFileStats(stats);
    } catch (error) {
      console.error('Failed to fetch file stats:', error);
    }
  };

  return (
    <div className="dashboard">
      <Row gutter={16}>
        <Col span={8}>
          <Card>
            <Statistic
              title="Total Files Uploaded"
              value={fileStats.totalFiles}
            />
          </Card>
        </Col>
        <Col span={8}>
          <Card>
            <Statistic
              title="Files Processed"
              value={fileStats.processedFiles}
            />
          </Card>
        </Col>
        <Col span={8}>
          <Card>
            <Statistic
              title="Files Pending Processing"
              value={fileStats.pendingFiles}
            />
          </Card>
        </Col>
      </Row>
    </div>
  );
};

export default Dashboard;
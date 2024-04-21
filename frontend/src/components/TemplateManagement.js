import React, { useState, useEffect } from 'react';
import { Button, Table, Modal, Form, Input } from 'antd';
import { templateService } from '../services/templateService';

const TemplateManagement = () => {
  const [templates, setTemplates] = useState([]);
  const [visible, setVisible] = useState(false);
  const [form] = Form.useForm();

  useEffect(() => {
    fetchTemplates();
  }, []);

  const fetchTemplates = async () => {
    const response = await templateService.getTemplates();
    setTemplates(response.data);
  };

  const handleAdd = () => {
    setVisible(true);
  };

  const handleOk = async () => {
    const values = await form.validateFields();
    await templateService.addTemplate(values);
    setVisible(false);
    fetchTemplates();
  };

  const handleCancel = () => {
    setVisible(false);
  };

  const handleDelete = async (id) => {
    await templateService.deleteTemplate(id);
    fetchTemplates();
  };

  return (
    <div>
      <Button type="primary" onClick={handleAdd}>
        Add Template
      </Button>
      <Table dataSource={templates}>
        <Table.Column title="Name" dataIndex="name" key="name" />
        <Table.Column title="Task" dataIndex="task" key="task" />
        <Table.Column
          title="Action"
          key="action"
          render={(text, record) => (
            <Button onClick={() => handleDelete(record.id)}>Delete</Button>
          )}
        />
      </Table>
      <Modal
        title="Add Template"
        visible={visible}
        onOk={handleOk}
        onCancel={handleCancel}
      >
        <Form form={form} layout="vertical">
          <Form.Item
            name="name"
            label="Template Name"
            rules={[{ required: true, message: 'Please input the template name!' }]}
          >
            <Input />
          </Form.Item>
          <Form.Item
            name="task"
            label="Associated Task"
            rules={[{ required: true, message: 'Please input the associated task!' }]}
          >
            <Input />
          </Form.Item>
        </Form>
      </Modal>
    </div>
  );
};

export default TemplateManagement;
﻿namespace analysis_paris.View {
    partial class DetailsItemControl {
        /// <summary> 
        /// 필수 디자이너 변수입니다.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary> 
        /// 사용 중인 모든 리소스를 정리합니다.
        /// </summary>
        /// <param name="disposing">관리되는 리소스를 삭제해야 하면 true이고, 그렇지 않으면 false입니다.</param>
        protected override void Dispose(bool disposing) {
            if (disposing && (components != null)) {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region 구성 요소 디자이너에서 생성한 코드

        /// <summary> 
        /// 디자이너 지원에 필요한 메서드입니다. 
        /// 이 메서드의 내용을 코드 편집기로 수정하지 마세요.
        /// </summary>
        private void InitializeComponent() {
            this.tableLayoutPanel1 = new System.Windows.Forms.TableLayoutPanel();
            this.lblDetailName = new System.Windows.Forms.Label();
            this.lblDetailValue = new System.Windows.Forms.Label();
            this.underBar = new System.Windows.Forms.Label();
            this.upperbar = new System.Windows.Forms.Label();
            this.tableLayoutPanel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // tableLayoutPanel1
            // 
            this.tableLayoutPanel1.BackColor = System.Drawing.Color.White;
            this.tableLayoutPanel1.ColumnCount = 2;
            this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 55.85023F));
            this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 44.14977F));
            this.tableLayoutPanel1.Controls.Add(this.lblDetailName, 0, 1);
            this.tableLayoutPanel1.Controls.Add(this.lblDetailValue, 1, 1);
            this.tableLayoutPanel1.Controls.Add(this.underBar, 0, 2);
            this.tableLayoutPanel1.Controls.Add(this.upperbar, 0, 0);
            this.tableLayoutPanel1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tableLayoutPanel1.Location = new System.Drawing.Point(0, 0);
            this.tableLayoutPanel1.Name = "tableLayoutPanel1";
            this.tableLayoutPanel1.RowCount = 3;
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 1F));
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 100F));
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 1F));
            this.tableLayoutPanel1.Size = new System.Drawing.Size(641, 36);
            this.tableLayoutPanel1.TabIndex = 0;
            // 
            // lblDetailName
            // 
            this.lblDetailName.Anchor = System.Windows.Forms.AnchorStyles.None;
            this.lblDetailName.AutoSize = true;
            this.lblDetailName.Font = new System.Drawing.Font("나눔고딕", 11F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(129)));
            this.lblDetailName.Location = new System.Drawing.Point(157, 12);
            this.lblDetailName.Margin = new System.Windows.Forms.Padding(0, 6, 0, 0);
            this.lblDetailName.Name = "lblDetailName";
            this.lblDetailName.Size = new System.Drawing.Size(44, 17);
            this.lblDetailName.TabIndex = 0;
            this.lblDetailName.Text = "학교?";
            this.lblDetailName.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // lblDetailValue
            // 
            this.lblDetailValue.Anchor = System.Windows.Forms.AnchorStyles.None;
            this.lblDetailValue.AutoSize = true;
            this.lblDetailValue.Font = new System.Drawing.Font("나눔고딕", 11F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(129)));
            this.lblDetailValue.Location = new System.Drawing.Point(475, 12);
            this.lblDetailValue.Margin = new System.Windows.Forms.Padding(0, 6, 0, 0);
            this.lblDetailValue.Name = "lblDetailValue";
            this.lblDetailValue.Size = new System.Drawing.Size(48, 17);
            this.lblDetailValue.TabIndex = 1;
            this.lblDetailValue.Text = "몇 개?";
            this.lblDetailValue.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // underBar
            // 
            this.underBar.AutoSize = true;
            this.underBar.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(172)))), ((int)(((byte)(172)))), ((int)(((byte)(172)))));
            this.tableLayoutPanel1.SetColumnSpan(this.underBar, 2);
            this.underBar.Dock = System.Windows.Forms.DockStyle.Fill;
            this.underBar.Location = new System.Drawing.Point(0, 35);
            this.underBar.Margin = new System.Windows.Forms.Padding(0);
            this.underBar.Name = "underBar";
            this.underBar.Size = new System.Drawing.Size(641, 1);
            this.underBar.TabIndex = 2;
            // 
            // upperbar
            // 
            this.upperbar.AutoSize = true;
            this.upperbar.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(17)))), ((int)(((byte)(17)))), ((int)(((byte)(17)))));
            this.tableLayoutPanel1.SetColumnSpan(this.upperbar, 2);
            this.upperbar.Dock = System.Windows.Forms.DockStyle.Fill;
            this.upperbar.Location = new System.Drawing.Point(6, 0);
            this.upperbar.Margin = new System.Windows.Forms.Padding(6, 0, 6, 0);
            this.upperbar.Name = "upperbar";
            this.upperbar.Size = new System.Drawing.Size(629, 1);
            this.upperbar.TabIndex = 3;
            this.upperbar.Visible = false;
            // 
            // DetailsItemControl
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.Controls.Add(this.tableLayoutPanel1);
            this.Margin = new System.Windows.Forms.Padding(0);
            this.Name = "DetailsItemControl";
            this.Size = new System.Drawing.Size(641, 36);
            this.tableLayoutPanel1.ResumeLayout(false);
            this.tableLayoutPanel1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.TableLayoutPanel tableLayoutPanel1;
        private System.Windows.Forms.Label lblDetailName;
        private System.Windows.Forms.Label lblDetailValue;
        private System.Windows.Forms.Label underBar;
        private System.Windows.Forms.Label upperbar;
    }
}

import { app } from "/scripts/app.js";
import { ComfyWidgets } from "/scripts/widgets.js";

app.registerExtension({
  name: "Comfy.ShowStringNode",
  async beforeRegisterNodeDef(nodeType, nodeData, app) {
    if (nodeData.name === "ShowStringNode") {
      function populate(text) {
        // Remove all widgets except the first one
        if (this.widgets) {
          for (let i = 1; i < this.widgets.length; i++) {
            this.widgets[i].onRemove?.();
          }
          this.widgets.length = 1;
        }

        // Ensure text is an array
        const v = Array.isArray(text) ? text : [text];

        // Create a widget for each text item
        for (const item of v) {
          if (item) {
            const w = ComfyWidgets["STRING"](this, "text", ["STRING", { multiline: true }], app).widget;
            w.inputEl.readOnly = true;
            w.inputEl.style.opacity = 0.6;
            w.value = item;
          }
        }

        // Resize the node if necessary
        this.onResize?.(this.computeSize());
        app.graph.setDirtyCanvas(true, false);
      }

      // When the node is executed, display the input text in the widget
      const onExecuted = nodeType.prototype.onExecuted;
      nodeType.prototype.onExecuted = function (message) {
        onExecuted?.apply(this, arguments);
        populate.call(this, message.text);
      };

      // Configure the node with initial values if available
      const onConfigure = nodeType.prototype.onConfigure;
      nodeType.prototype.onConfigure = function () {
        onConfigure?.apply(this, arguments);
        if (this.widgets_values?.length) {
          populate.call(this, this.widgets_values);
        }
      };
    }
  },
});
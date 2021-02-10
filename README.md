# SAF Patterns

**SAF Patterns** — это плагин для SmartApp Framework который позволяет использовать паттерны на пользовательский ввод.
Механизм матчинга паттернов реализован на C#, плагин требует Mono/.NET

## Оглавление
   * [Установка](#Установка)
   * [Новый функционал](#Новый)
   * [Документация](#Документация)
   * [Обратная связь](#Обратная)

____

# Установка

Для работы плагина требуется [Pythonnet](http://pythonnet.github.io). Подробная инструкция по установке описана на [wiki проекта](https://github.com/pythonnet/pythonnet/wiki/Installation).

Установить сам плагин можно из git.

```bash
python -m pip install git+https://github.com/sberdevices/saf_patterns@main
```

# Новый функционал

Плагин содержат один новый Requirement "pattern" и Action "pattern_resolve_scenario"

С помощью pattern Requirement можно задать условие на входящий текст

```json
{
  "type": "pattern",
  "patterns": [
    "[бывш~ прежн~] .{0,3} ([телефон~ номер]+ | сим карта)",
    "([телефон~ номер]+ | сим карта) .{0,3} [бывш~ прежн~]"
  ]
}
```
patterns_resolve_scenario позволяет выбрать сценарий с наиболее подходящим паттерном

```json
{
  "type": "pattern_resolve_scenario",
  "scenarios": {
    "scenario_1": [
      "some_pattern"
    ],
    "scenario_2": [
      "some_pattern"
    ]
  },
  "else": {
    "type": "some_fallback_action"
  }
}
```

# Документация

?????

# Обратная связь

C вопросами и предложениями пишите нам по адресу developer@sberdevices.ru или вступайте в наш Telegram канал - [SmartApp Studio Community](https://t.me/smartapp_studio). 
